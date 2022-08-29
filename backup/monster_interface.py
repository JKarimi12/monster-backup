from urllib.parse import urljoin

from decouple import config
import requests


class MonsterInterface:
    PUBLIC_URL = config('public_url')
    API_KEY = config('api_key')

    @classmethod
    def create_bucket(cls, bucket_name):
        return requests.put(
            urljoin(cls.PUBLIC_URL, bucket_name),
            headers={
                'Content-Length': '0',
                'X-API-KEY': cls.API_KEY
            }
        )

    @classmethod
    def ls_bucket(cls, bucket_name):
        return requests.get(
            urljoin(cls.PUBLIC_URL, bucket_name),
            headers={
                'X-API-KEY': cls.API_KEY
            }
        )

    @classmethod
    def crud_bucket_meta_data(cls, bucket_name, meta_data):
        return requests.post(
            urljoin(cls.PUBLIC_URL, bucket_name),
            headers={
                'X-API-KEY': cls.API_KEY,
                **meta_data
            }
        )

    @classmethod
    def get_bucket_meta_data(cls, bucket_name):
        return requests.head(
            urljoin(cls.PUBLIC_URL, bucket_name),
            headers={
                'X-API-KEY': cls.API_KEY
            }
        )

    @classmethod
    def rm_bucket(cls, bucket_name):
        return requests.delete(
            urljoin(cls.PUBLIC_URL, bucket_name),
            headers={
                'X-API-KEY': cls.API_KEY
            }
        )

    @classmethod
    def get_obj(cls, bucket_name, file_name):
        return requests.get(
            urljoin(cls.PUBLIC_URL, f'{bucket_name}/{file_name}'),
            headers={
                'X-API-KEY': cls.API_KEY
            }
        )

    @classmethod
    def create_obj(cls, bucket_name, file_name, data):
        return requests.put(
            urljoin(cls.PUBLIC_URL, f'{bucket_name}/{file_name}'),
            data=data,
            headers={
                'X-API-KEY': cls.API_KEY,
                'Content-Type': 'text/html', #todo: maybe should change
                'Charset': 'UTF-8',
            }
        )

    @classmethod
    def create_obj_from_file(cls, bucket_name, file_name, path):
        with open(path) as f:
            return requests.put(
                urljoin(cls.PUBLIC_URL, f'{bucket_name}/{file_name}'),
                data=f,
                headers={
                    'X-API-KEY': cls.API_KEY,
                    'Content-Type': 'text/html', #todo: maybe should change
                    'Charset': 'UTF-8',
                }
            )

    @classmethod
    def cp_obj(cls, bucket_name, file_name, dest):
        return requests.post(
            urljoin(cls.PUBLIC_URL, f'{bucket_name}/{file_name}'),
            headers={
                'X-API-KEY': cls.API_KEY,
                'Destination': dest,
            }
        )

    @classmethod
    def rm_obj(cls, bucket_name, file_name):
        return requests.delete(
            urljoin(cls.PUBLIC_URL, f'{bucket_name}/{file_name}'),
            headers={
                'X-API-KEY': cls.API_KEY,
            }
        )

    @classmethod
    def get_meta_data_of_obj(cls, bucket_name, file_name):
        return requests.head(
            urljoin(cls.PUBLIC_URL, f'{bucket_name}/{file_name}'),
            headers={
                'X-API-KEY': cls.API_KEY,
            }
        )

    @classmethod
    def crud_meta_data_of_obj(cls, bucket_name, file_name, meta_data):
        return requests.post(
            urljoin(cls.PUBLIC_URL, f'{bucket_name}/{file_name}'),
            headers={
                'X-API-KEY': cls.API_KEY,
                **meta_data
            }
        )

