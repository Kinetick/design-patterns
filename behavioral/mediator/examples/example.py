from ..pattern.base import BaseMessageExchanger, BaseService

common_exchanger = BaseMessageExchanger()
test_service_1 = BaseService(
    service_name="test_1", message_exchanger=common_exchanger
)
test_service_2 = BaseService(
    service_name="test_2", message_exchanger=common_exchanger
)
test_service_3 = BaseService(
    service_name="test_3", message_exchanger=common_exchanger
)
test_service_4 = BaseService(
    service_name="test_4", message_exchanger=common_exchanger
)
test_service_5 = BaseService(
    service_name="test_5", message_exchanger=common_exchanger
)

common_exchanger.register_service(
    topic=test_service_1.name, service=test_service_3
)
common_exchanger.register_service(
    topic=test_service_1.name, service=test_service_4
)
common_exchanger.register_service(
    topic=test_service_3.name, service=test_service_1
)
common_exchanger.register_service(
    topic=test_service_5.name, service=test_service_3
)
common_exchanger.register_service(
    topic=test_service_5.name, service=test_service_4
)
