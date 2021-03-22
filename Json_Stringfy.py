import json
import pdb




    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)




