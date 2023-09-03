import json

from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

# GraphQLサーバーのエンドポイントURL
url = 'https://example.com/graphql'

_headers = {
    "Content-Type": "application/graphql",
    "x-api-key": "XXXXXXXXXXXXXXXXXXXX",
}

# GraphQLクライアントをセットアップ
transport = RequestsHTTPTransport(
    url=url,
    headers=_headers,
    # use_json=True,
)

# スキーマファイルを読み込む場合
# with open('./schema.graphql') as f:
#     schema_str = f.read()
# client = Client(transport=transport, fetch_schema_from_transport=True, schema=schema_str)

client = Client(transport=transport, fetch_schema_from_transport=True)

# ミューテーションクエリを定義
mutation_query = gql("""
    mutation PublishData($name: String!, $data: AWSJSON!) {
        publish(name: $name, data: $data) {
            name
            data
        }
    }
""")

import json
# ミューテーションの変数を定義
mutation_variables = {
    'name': 'robots',
    'data': json.dumps({
        'key1': 'value1',
        'key2': 'value2'
    })
}

# ミューテーションを実行
result = client.execute(mutation_query, variable_values=mutation_variables)

# 結果を表示
print(result)
