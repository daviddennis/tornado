import json
from datetime import date
from copy import copy
from decimal import Decimal

from tornado import gen
from tornado import web
from tornado.web import HTTPError
from tornado import escape
import psycopg2
from constants import (TEST_DATA, RESPONSE_TEMPLATE, LOOKUP_REQ_FIELDS,
    DEVICE_FIELDS, SUCCESS)
from queries import (LOOKUP_BUNDLE_BY_TIME, INSERT_BUNDLE)


class BaseHandler(web.RequestHandler):
    @property
    def db(self):
        return self.application.db


class DeviceHandler(BaseHandler):
    @gen.coroutine
    def get(self):
        # lookup bundles

        data = self._validate_lookup()

        values = data.values()
        query = copy(LOOKUP_BUNDLE_BY_TIME)
        query = query.format(**data)

        try:
            f1 = self.db.execute(query)
            yield [f1]
            cursor1 = f1.result()
        except (psycopg2.Warning, psycopg2.Error) as e:
            # log postgres error
            raise HTTPError(reason='Something went wrong, please try back later.' % field_name,
                            status_code=500)
        else:
            response = copy(RESPONSE_TEMPLATE)
            response['status'] = SUCCESS
            response['response'] = []
            db_data = cursor1.fetchall()
            for record in db_data:
                if record:
                    resp_data = {}
                    for i,val in enumerate(record):
                        field_name = DEVICE_FIELDS[i]
                        val = str(val) if isinstance(val, Decimal) else val
                        resp_data[field_name] = val
                    response['response'].append(resp_data)
            self.write(json.dumps(response))
 
    @gen.coroutine
    def post(self):
        # upload bundles
        data = escape.json_decode(self.request.body)
        self._validate_create(data)

        query = copy(INSERT_BUNDLE)     
        query = query.format(**data)
        
        try:
            self.db.execute(query)
        except Exception as e:
            # log error
            raise HTTPError(reason='Something went wrong, please try back later.',
                            status_code=500)
        else:
            resp_json = copy(RESPONSE_TEMPLATE)
            resp_json['status'] = SUCCESS
            resp_json['response'] = data
            self.write(json.dumps(resp_json))

    def _validate_lookup(self):
        data = {}
        for field_name in LOOKUP_REQ_FIELDS:
            val = self.get_arguments(field_name)
            val = val[0] if val is not None else None
            if val:
                data[field_name] = val
            else:
                raise HTTPError(reason='Field "%s" is null' % field_name,
                                status_code=422)
        return data

    def _validate_create(self, data):
        for field_name in DEVICE_FIELDS:
            val = data.get(field_name)
            if val:
                data[field_name] = val
            else:
                print(field_name, val)
                raise HTTPError(reason='Field "%s" is null' % field_name,
                                status_code=422)
        return data


class DeviceLoadHandler(BaseHandler):
    @gen.coroutine
    def get(self):

        resp_json = []
        for data in TEST_DATA:
            query = copy(INSERT_BUNDLE)     
            query = query.format(**data)
            
            try:
                self.db.execute(query)
            except Exception as e:
                # log error
                raise HTTPError(reason='Something went wrong, please try back later.',
                                status_code=500)
            else:
                resp_record = copy(RESPONSE_TEMPLATE)
                resp_record['status'] = SUCCESS
                resp_json.append(resp_record)
        self.write(json.dumps(resp_json))

