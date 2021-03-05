from dacite import from_dict

from pokemontcgsdk.restclient import RestClient
from pokemontcgsdk.config import __endpoint__

class QueryBuilder():
    def __init__(self, type):
        self.params = {}
        self.type = type

    def find(self, id):
        """Get a resource by its id
        
        Args:
            id (string): Resource id    
        Returns:
            object: Instance of the resource type
        """
        url = "{}/{}/{}".format(__endpoint__, self.type.RESOURCE, id)
        response = RestClient.get(url)['data']
        return from_dict(self.type, response)

    def where(self, **kwargs):
        """Adds a parameter to the dictionary of query parameters
        
        Args:
            **kwargs: Arbitrary keyword arguments.
        Returns:
            list of object: List of resource objects
        """
        for key, value in kwargs.items():
            self.params[key] = value

        return self.all()

    def all(self):
        """Get all resources, automatically paging through data

        Returns:
            list of object: List of resource objects
        """
        list = []
        page = 1
        fetch_all = True
        url = "{}/{}".format(__endpoint__, self.type.RESOURCE)

        if 'page' in self.params:
            page = self.params['page']
            fetch_all = False

        while True:
            response = RestClient.get(url, self.params)['data']
            if len(response) > 0:
                for item in response:
                    list.append(from_dict(self.type, item))

                if not fetch_all:
                    break
                else:
                    page += 1
                    self.where(page=page)
            else:
                break

        return list
        
    def array(self):
        """Get all resources and return the result as an array

        Returns:
            array of str: Array of resources
        """
        url = "{}/{}".format(__endpoint__, self.type.RESOURCE)
        return RestClient.get(url, self.params)['data']