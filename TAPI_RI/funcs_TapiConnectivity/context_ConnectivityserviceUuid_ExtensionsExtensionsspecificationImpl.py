import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_ConnectivityserviceUuid_ExtensionsExtensionsspecificationImpl:

    @classmethod
    def get(cls, uuid, extensionsSpecification):
        print 'handling get'
        if uuid in be.Context._connectivityService:
            if extensionsSpecification in be.Context._connectivityService[uuid]._extensions:
                return be.Context._connectivityService[uuid]._extensions[extensionsSpecification]
            else:
                raise KeyError('extensionsSpecification')
        else:
            raise KeyError('uuid')
