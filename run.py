"""

加权随机抽奖

"""

import logging
from typing import List
import random

from dataclasses import dataclass,field

@dataclass
class Person(object):
    name:str = field()
    score:int = field()

    def __str__(self):

        return f"姓名:{self.name},积分：{self.score}"

def get_name_score(file_name)->List[Person]:
    """
    获取组合
    :param file_name:
    :return:
    """
    data_back = []
    with open(file_name,"r") as f:
        while True:
            data = f.readline()
            if not data:
                break
            name,score = data.split(",")
            score = int(score)
            person = Person(name,score)
            data_back.append(person)
    return data_back

def get_rand_person(persons:List[Person]):
    logging.info("参与抽奖人员")
    logging.info(persons)

    data_tmp = [person.score for person in persons]
    value_sorces = sum(data_tmp)
    logging.info(f"本次投入总分：{value_sorces}")

    rand_value = random.randint(0,value_sorces)
    logging.info(f"本次抽奖获得的随机数:{rand_value}")
    last_value = 0
    data_back = None
    i_value = 0
    for i in range(len(persons)):
        person_tmp:Person = persons[i]
        value_tmp = last_value+person_tmp.score
        if value_tmp>=rand_value:
            data_back = person_tmp
            i_value = i
            break
        last_value = value_tmp
    if data_back is not None:
        logging.info(f"抽到：{data_back}")
        persons.pop(i_value)
        return data_back
    else:

        raise Exception("出现错误")


def make_data(file_name:str,nums:int=None):
    persons:List[Person] = get_name_score(file_name)
    persons = sorted(persons, key=lambda a: a.score)
    if nums is None:
        nums = len(persons)
    else:
        nums = min(len(persons),nums)

    for _ in range(nums):
        person:Person = get_rand_person(persons)
        logging.info('='*10)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    file_name = "data.csv"
    make_data(file_name)