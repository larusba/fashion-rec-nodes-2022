import pyarrow as pa
import pyarrow.flight as flight
import base64

token = base64.b64encode(f'neo4j:ms8!r#%E&Rs27+Q7'.encode('utf8'))
options = flight.FlightCallOptions(headers=[
            (b'authorization', b'Basic ' + token)
        ])
client = pa.flight.connect("grpc+tcp://localhost:8491")
print(client.list_actions(options=options))
reader = client.do_get(flight.Ticket("""{
    "graph_name": "prova",
    "database_name": "hem", 
    "procedure_name": "gds.graph.streamNodeProperties",
    "configuration": { 
        "node_labels": ["Article", "Customer"],
        "node_properties": ["article_id","age"]
        }
    }""".encode('utf-8')), options = options)
table = reader.read_all()

print(table)
