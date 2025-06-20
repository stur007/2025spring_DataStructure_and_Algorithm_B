from collections import defaultdict
AC_questions = defaultdict(set)
submission_times = defaultdict(int)
m = int(input())
for _ in range(m):
    name, question, result = input().split(',')
    if result == 'yes':
        AC_questions[name].add(question)
    submission_times[name] += 1
ranks = []
for name in submission_times:
    ranks.append((len(AC_questions[name]), submission_times[name], name))
ranks.sort(key = lambda x:(-x[0], x[1], x[2]))
for i in range(12):
    if i < len(ranks):
        print(f'{i+1} {ranks[i][2]} {ranks[i][0]} {ranks[i][1]}')
    else:
        break