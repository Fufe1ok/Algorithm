from datetime import datetime
from Sorting import selection_sort_by_table
from Sorting import merge_sort_by_max_dishes
from Restaurants import Restaraunts

def time_of_working(start_time, finish_time):
    return finish_time - start_time

if __name__ == "__main__":
    restaraunts_list = []

    restaraunts1 = Restaraunts("name1", 12, 35)
    restaraunts2 = Restaraunts("name2", 64, 65)
    restaraunts3 = Restaraunts("name2", 98, 47)
    restaraunts4 = Restaraunts("name2", 123, 36)
    restaraunts5 = Restaraunts("name2", 98, 72)
    restaraunts6 = Restaraunts("name2", 15, 86)
    restaraunts7 = Restaraunts("name2", 21, 45)
    restaraunts8 = Restaraunts("name2", 65, 26)
    restaraunts9 = Restaraunts("name2", 18, 74)

    restaraunts_list.append(restaraunts1)
    restaraunts_list.append(restaraunts2)
    restaraunts_list.append(restaraunts3)
    restaraunts_list.append(restaraunts4)
    restaraunts_list.append(restaraunts5)
    restaraunts_list.append(restaraunts6)
    restaraunts_list.append(restaraunts7)
    restaraunts_list.append(restaraunts8)
    restaraunts_list.append(restaraunts9)

    print("Restaraunts:\n" + restaraunts_list.__str__())
    start = datetime.now().microsecond
    print("\nSelection sort:\n"+selection_sort_by_table(restaraunts_list).__str__())
    finish = datetime.now().microsecond
    print("Work time: " + time_of_working(start, finish).__str__())
    start = datetime.now().microsecond
    print("\nMerge sort:\n" + merge_sort_by_max_dishes(restaraunts_list).__str__())
    finish = datetime.now().microsecond
    print("\nWorking time:\n " + time_of_working(start, finish).__str__())

