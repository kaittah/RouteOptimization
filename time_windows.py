from datetime import datetime, timezone, timedelta

est_tz = timezone(offset=timedelta(hours=-4))

delivery_times = {
                    'min': int(datetime(2020, 10, 1, 12, 0, tzinfo = est_tz).timestamp()),
                    '11:30': int(datetime(2020, 10, 1, 11, 30, tzinfo = est_tz).timestamp()),
                    '11:45': int(datetime(2020, 10, 1, 11, 45, tzinfo = est_tz).timestamp()),
                    '12:00': int(datetime(2020, 10, 1, 12, 0, tzinfo = est_tz).timestamp()),
                    '12:15': int(datetime(2020, 10, 1, 12, 15, tzinfo = est_tz).timestamp()),
                    '12:30': int(datetime(2020, 10, 1, 12, 30, tzinfo = est_tz).timestamp()),
                    '12:45': int(datetime(2020, 10, 1, 12, 45, tzinfo = est_tz).timestamp()),
                    '1:00': int(datetime(2020, 10, 1, 13, 0, tzinfo = est_tz).timestamp()),
                    '1:15': int(datetime(2020, 10, 1, 13, 15, tzinfo = est_tz).timestamp()), 
                    'max': int(datetime(2020, 10, 1, 13, 0, tzinfo = est_tz).timestamp())
}

fixed_time_windows = {  'A':[
                                [delivery_times['12:00'], delivery_times['1:00']]
                            ],
                        'B':[
                                [delivery_times['12:00'], delivery_times['12:30']],
                                [delivery_times['12:30'], delivery_times['1:00']]
                            ],
                        'C':[
                                [delivery_times['12:00'], delivery_times['12:30']],
                                [delivery_times['12:15'], delivery_times['12:45']],  
                                [delivery_times['12:30'], delivery_times['1:00']]
                            ]
                        }