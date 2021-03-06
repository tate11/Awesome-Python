﻿from flask import Flask
from flask_cors import CORS
from flask_restful_swagger_2 import swagger, Api, Resource, request
# pip install flask-restful-swagger-2
# Swagger라는 멋진 API 관리 툴이 있는데, flask-restful-swagger 패키지를 이용해서 Flask-restful 기반으로 문서화 가능하다
# 실제로 라이브러리 내부에서는 Swagger에 관련된 작업 후 flask-restful로 라우팅 처리를 넘긴다

app = Flask(__name__)
CORS(app)
# Swagger에는 CORS 지원이 필요

api = Api(app, api_version='1.0', title='Sample Server', description='This is Sample API Server!')
# Swagger Docs에 보여질 API 버전, 타이틀, description
# api_spec_url 파라미터도 있음(기본값은 /api/swagger)
# 부가적인 것들은 Api 클래스를 참조하도록 하자


class Sample(Resource):
    @swagger.doc({
        'tags': ['user'],
        # 태그를 기준으로 API 정리할 수 있다

        'description': 'Returns hello world!',
        # API description

        'parameters': [
            # 파라미터 리스트
            {
                'name': 'id',
                # 파라미터의 key name

                'description': 'Identifier',
                # 파라미터 description

                'in': 'path',
                # 파라미터가 들어갈 곳
                # must be path, query, header, body or formData

                'type': 'int',
                # 타입

                'required': True
                # 필수 여부
            },
            {
                'name': 'test_form',
                'description': 'Data for test',
                'in': 'formData',
                'type': 'any'
            }
        ],
        'responses': {
            '200': {
                # status code

                'description': 'Success',
                # Response description

                'examples': {
                    # Example value
                    
                    'application/json': {
                        'id': 1,
                        'form_data': 'hello?'
                    }
                }
            }
        }
     })
    def post(self, id):
        return {
            'id': id,
            'form_data': request.form.get('test_form')
        }, 200

api.add_resource(Sample, '/sample/<id>')

if __name__ == '__main__':
    app.run(debug=True)

# http://petstore.swagger.io/?url=http://localhost:5000/api/swagger.json
