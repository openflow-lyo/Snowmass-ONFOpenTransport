import os.path, sys
import json
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be
from objects_TapiConnectivity.connection import Connection, Direction
from objects_TapiConnectivity._connectivityServiceSchema import _connectivityServiceSchema 
from objects_TapiConnectivity.operationalStatePac import OperationalStatePac
from objects_TapiConnectivity.layerProtocol import Layerprotocolname
from objects_TapiConnectivity.connectionPort import ConnectionPort

class Context_ConnectivityserviceUuidImpl:

    @classmethod
    def put(cls, uuid, _connectivityserviceschema):
        print str(_connectivityserviceschema)
        print 'handling put'
        print 'We are not modifying connection...'
        be.Context._connectivityService[uuid] = _connectivityserviceschema

    @classmethod
    def post(cls, uuid, _connectivityserviceschema):
        print str(_connectivityserviceschema)
        print 'not handling post'
        


    @classmethod
    def delete(cls, uuid):
        print 'handling delete'
        if uuid in be.Context._connectivityService:
            print 'first we need to delete the related connection'
            be.remove_flow(uuid)
            for con_uuid_str in be.Context._connectivityService[uuid]._connection :
                con_uuid = con_uuid_str.split('restconf/config/Context/_connection/')[1]
                con_uuid = con_uuid.split('/')[0]
                print 'Removing connection: ' + con_uuid
                del be.Context._connection[con_uuid]
            del be.Context._connectivityService[uuid]
        else:
            raise KeyError('uuid')

    @classmethod
    def get(cls, uuid):
        print 'handling get'
        if uuid in be.Context._connectivityService:
            return be.Context._connectivityService[uuid]
        else:
            raise KeyError('uuid')
