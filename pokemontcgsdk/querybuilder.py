from dacite import from_dict

from pokemontcgsdk.restclient import RestClient
from pokemontcgsdk.config import __endpoint__

class QueryBuilder():
    def __init__(self, type, transform=None):
        self.params = {}
        self.type = type
        self.transform = transform

    def find(self, id):
        """Get a resource by its id
        
        Args:
            id (string): Resource id    
        Returns:
            object: Instance of the resource type
        """
        url = "{}/{}/{}".format(__endpoint__, self.type.RESOURCE, id)
        response = RestClient.get(url)['data']

        # Transform json keys into names that are safe for python properties
        if self.transform:
            response = self.transform(response)

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
        fetch_all = True
        url = "{}/{}".format(__endpoint__, self.type.RESOURCE)

        if 'page' in self.params:
            fetch_all = False
        else:
            self.params['page'] = 1

        while True:
            response = RestClient.get(url, self.params)['data']
            if len(response) > 0:
                if self.transform:
                    response = [self.transform(i) for i in response]

                list.extend([from_dict(self.type, item) for item in response])

                if fetch_all:
                    self.params['page'] += 1
                else:
                    break
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