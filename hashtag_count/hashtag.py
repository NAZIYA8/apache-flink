'''
@Author: Naziya

@Date: 2021-10-12

@Last Modified by: Naziya

@Last Modified : 2021-10-12

@Title : Program Aim is to perform hastag wordcount using flink.
'''

import os
import random
from LoggerFormat import logger
from pyflink.table import DataTypes, TableEnvironment, EnvironmentSettings
from pyflink.table.descriptors import Schema, OldCsv ,FileSystem

from pyflink.table.expressions import lit

## Creating config
settings = EnvironmentSettings.new_instance().in_batch_mode().use_blink_planner().build()
t_env = TableEnvironment.create(settings)


def hashtag_count():
    try:
        input_file = "/home/naziya/apache-flink/hashtag_count/input.txt"
        output_file = "/home/naziya/apache-flink/hashtag_count/output.csv"

        if os.path.isfile(output_file):
            os.remove(output_file)

        hashtags = ['#hello', '#python', '#world']
        num_tweets = 1000
        with open(input_file, 'w') as f:
            for tweet in range(num_tweets):
                f.write('%s\n' % (random.choice(hashtags)))

        t_env.get_config().get_configuration().set_string("parallelism.default", "1")
        t_env.connect(FileSystem().path(input_file)) \
                .with_format(OldCsv()
                        .field('word', DataTypes.STRING())) \
                .with_schema(Schema()
                        .field('word', DataTypes.STRING())) \
                .create_temporary_table('mySource')

        t_env.connect(FileSystem().path(output_file)) \
                .with_format(OldCsv()
                        .field_delimiter('\t')
                        .field('word', DataTypes.STRING())
                        .field('count', DataTypes.BIGINT())) \
                .with_schema(Schema()
                        .field('word', DataTypes.STRING())
                        .field('count', DataTypes.BIGINT())) \
                .create_temporary_table('mySink')

        tab = t_env.from_path('mySource')
        tab.group_by(tab.word) \
        .select(tab.word, lit(1).count) \
        .execute_insert('mySink').wait()      

    except Exception as e:
            logger.error(e)

hashtag_count()