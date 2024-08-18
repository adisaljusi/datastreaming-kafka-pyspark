#!/usr/bin/env python

from faker import Faker
import time

def create_sample_date(faker: Faker, id: int):
    return {
        "id": id,
        "name": faker.unique.name(),
        "address": faker.unique.address(),
        "timestamp": faker.iso8601(),
    }


# def

if __name__ == "__main__":
    faker = Faker()
    for i in range(0, 10):
        print(create_sample_date(faker, i))
        time.sleep(5)
