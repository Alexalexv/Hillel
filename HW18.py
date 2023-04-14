test_design_writers = [1, 3, 5]
scripters = [2, 3, 4, 6, 7, 8]
reviewers = [1, 2, 3, 9, 10]
out_of_office_today = [2, 5, 6, 1]

test_design_writers_set = set(test_design_writers)
scripters_set = set(scripters)
reviewers_set = set(reviewers)
out_of_office_today_set = set(out_of_office_today)

all_set = test_design_writers_set | scripters_set | reviewers_set
only_scripters_set = scripters_set - (test_design_writers_set | reviewers_set)
at_work_set = all_set - all_set.intersection(out_of_office_today_set)
review_and_scripters_set = scripters_set.intersection(reviewers_set)
review_and_scripters_at_work_set = at_work_set.intersection(review_and_scripters_set)

all_ = sorted(list(all_set))
only_scripters = sorted(list(only_scripters_set))
at_work = sorted(list(at_work_set))
review_and_scripters_at_work = sorted(list(review_and_scripters_at_work_set))

print(all_)
print(only_scripters)
print(at_work)
print(review_and_scripters_at_work)
