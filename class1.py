import re
import random
import jieba
import jieba.posseg as pos
jieba.add_word("放假", tag="n")


def get_rule_list(rule):
    rule_list = []
    for k in list(rule.keys()):
        rule_list.append(''.join(re.findall('x(.*?)\?', k)))

    for i in range(len(rule_list) - 1):  # 冒泡排序，最大匹配
        for j in range(len(rule_list) - 1):
            if len(rule_list[j]) < len(rule_list[j + 1]):
                rule_list[j], rule_list[j + 1] = rule_list[j + 1], rule_list[j]
    return rule_list


def pat_match(saying, rule, rule_list):
    n_list = []
    answer = ''
    for i in rule_list:
        if i in saying:
            for k in list(rule.keys()):
                if i in k:
                    answer += ''.join(random.choice(list(rule[k])))
                    break
            for s in saying.split(i):
                if s == '':
                    n_list.append('noun')
                    continue
                for w, f in pos.cut(s):
                    if f == 'n':
                         n_list.append(w)
            break
    pat = dict(zip(['?x', '?y'], n_list))
    for p in pat.keys():
        answer = answer.replace(p, pat[p])
    return answer


rules = {'?x我想?y': ['你觉得?y有什么意义呢？', '为什么你想?y？', '你可以想想你很快就可以?y了。'],
         '?x我想要?y': ['不，你不想要?y', '你写完作业才能?y']}


def main():
    rule_list = get_rule_list(rules)
    saying = '老师，我想放假。'
    print(saying)
    answer = pat_match(saying, rules, rule_list)
    print(answer)
    saying1 = '我想要出去玩。'
    print(saying1)
    answer1 = pat_match(saying1, rules, rule_list)
    print(answer1)


if __name__ == '__main__':
    main()

