class Customer:
    def __init__(self, verb: str, key: str, event_time: str, last_name: str, adr_city: str,
                 adr_state: str) -> None:
        self.verb = verb
        self.key = key
        self.event_time = event_time
        self.last_name = last_name
        self.adr_city = adr_city
        self.adr_state = adr_state


class SiteVisit:
    def __init__(self, verb: str, key: str, event_time: str, customer_id: str, tags: dict) -> None:
        self.verb = verb
        self.key = key
        self.event_time = event_time
        self.customer_id = customer_id
        self.tags = tags


class Image:
    def __init__(self, verb: str, key: str, event_time: str, customer_id: str, camera_make: str,
                 camera_model: str) -> None:
        self.verb = verb
        self.key = key
        self.event_time = event_time
        self.customer_id = customer_id
        self.camera_make = camera_make
        self.camera_model = camera_model


class Order:
    def __init__(self, verb: str, key: str, event_time: str, customer_id: str, total_amount: str) -> None:
        self.verb = verb
        self.key = key
        self.event_time = event_time
        self.customer_id = customer_id
        self.total_amount = total_amount


