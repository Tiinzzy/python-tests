import os

class OidGenerator:

    @staticmethod
    def get_new():
        LAST_OID_FILENAME = "/home/tina/Documents/python/python-tests/Learning-Python/netflix-model/resources/last-oid.txt"
        new_id = -1

        try:
            with open(LAST_OID_FILENAME, 'r') as file:
                content = file.read()
                new_id = int(content)
                new_id += 1

            with open(LAST_OID_FILENAME, 'w') as file:
                file.write(str(new_id))

        except Exception as e:
            raise RuntimeError(e)

        return new_id
