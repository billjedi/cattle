from common_fixtures import *  # NOQA
from cattle import ApiError


def test_lb_config_create_wo_listener(admin_client):
    config = admin_client.create_loadBalancerConfig(name=random_str())
    config = admin_client.wait_success(config)

    assert config.state == 'active'


def test_lb_config_add_listener(admin_client, super_client):
    config, listener = _create_config_and_listener(admin_client)

    # add listener to the config
    config = config.addlistener(loadBalancerListenerId=listener.id)
    config = admin_client.wait_success(config)

    assert config.state == 'active'
    lbconfigmap = super_client. \
        list_loadBalancerConfigListenerMap(loadBalancerListenerId=listener.id,
                                           loadBalancerConfigId=config.id)

    assert len(lbconfigmap) == 1
    assert lbconfigmap[0].state == 'active'


def test_create_config_add_invalid_listener(admin_client):
    config, listener = _create_config_and_listener(admin_client)

    with pytest.raises(ApiError) as e:
        config = config.addlistener(loadBalancerListenerId='dummy')

    assert e.value.error.status == 422
    assert e.value.error.code == 'InvalidReference'
    assert e.value.error.fieldName == 'loadBalancerListenerId'


def test_lb_config_add_listener_wo_listenerId(admin_client):
    config, listener = _create_config_and_listener(admin_client)

    # add listener to the config without specifying the id
    with pytest.raises(ApiError) as e:
        config = config.addlistener()

    assert e.value.error.status == 422
    assert e.value.error.code == 'MissingRequired'
    assert e.value.error.fieldName == 'loadBalancerListenerId'


def test_lb_config_remove_listener(admin_client, super_client):
    config, listener = _create_config_and_listener(admin_client)

    # add listener to the config
    config = config.addlistener(loadBalancerListenerId=listener.id)
    config = admin_client.wait_success(config)

    assert config.state == 'active'
    lbconfigmap = super_client. \
        list_loadBalancerConfigListenerMap(loadBalancerListenerId=listener.id,
                                           loadBalancerConfigId=config.id)

    assert len(lbconfigmap) == 1

    # remove listener from the config
    config = config. \
        removelistener(loadBalancerListenerId=listener.id)
    config = admin_client.wait_success(config)

    lbconfigmap = super_client. \
        list_loadBalancerConfigListenerMap(loadBalancerListenerId=listener.id,
                                           loadBalancerConfigId=config.id)

    assert lbconfigmap[0].state == 'removed'


def test_lb_config_delete_listener_wo_listenerId(admin_client):
    config, listener = _create_config_and_listener(admin_client)

    # remove listener to the config without specifying the id
    with pytest.raises(ApiError) as e:
        config = config.removelistener()

    assert e.value.error.status == 422
    assert e.value.error.code == 'MissingRequired'
    assert e.value.error.fieldName == 'loadBalancerListenerId'


def test_lb_config_update(admin_client):
    config = admin_client.create_loadBalancerConfig(name='config1')
    config = admin_client.wait_success(config)

    config = admin_client.update(config, name='newName')
    assert config.name == 'newName'


def test_lb_config_remove(admin_client):
    config = admin_client.create_loadBalancerConfig(name=random_str())
    config = admin_client.wait_success(config)

    config = admin_client.wait_success(admin_client.delete(config))

    assert config.state == 'removed'


def test_lb_config_listener_remove(admin_client, super_client):
    # create config and listener
    config, listener = _create_config_and_listener(admin_client)

    # add a listener to the config
    config = config.addlistener(loadBalancerListenerId=listener.id)
    config = admin_client.wait_success(config)

    # delete the listener
    listener = admin_client.wait_success(admin_client.delete(listener))
    assert listener.state == 'removed'

    # verify that the mapping is gone
    lbconfigmap = super_client. \
        list_loadBalancerConfigListenerMap(loadBalancerListenerId=listener.id,
                                           loadBalancerConfigId=config.id)

    assert lbconfigmap[0].state == "removed"


def test_lb_listener_remove(admin_client, super_client):
    # create a listener
    listener = _create_valid_listener(admin_client)

    # create 2 configs, add listener to both of them
    config1 = admin_client. \
        create_loadBalancerConfig(name=random_str())
    config1 = admin_client.wait_success(config1)
    config1 = config1. \
        addlistener(loadBalancerListenerId=listener.id)
    config1 = admin_client.wait_success(config1)

    config2 = admin_client. \
        create_loadBalancerConfig(name=random_str())
    config2 = admin_client.wait_success(config2)
    config2 = config2. \
        addlistener(loadBalancerListenerId=listener.id)
    config2 = admin_client.wait_success(config2)

    # delete the listener
    listener = admin_client.wait_success(admin_client.delete(listener))
    assert listener.state == 'removed'

    # verify that the mapping is gone for both configs
    lbconfigmap = super_client. \
        list_loadBalancerConfigListenerMap(loadBalancerListenerId=listener.id,
                                           loadBalancerConfigId=config1.id)

    assert lbconfigmap[0].state == "removed"

    lbconfigmap = super_client. \
        list_loadBalancerConfigListenerMap(loadBalancerListenerId=listener.id,
                                           loadBalancerConfigId=config2.id)

    assert lbconfigmap[0].state == "removed"


def test_lb_config_remove_w_listeners(admin_client, super_client):
    # create a listener
    listener = _create_valid_listener(admin_client)

    # create 2 configs, add listener to both of them
    config1 = admin_client. \
        create_loadBalancerConfig(name=random_str())
    config1 = admin_client.wait_success(config1)
    config1 = config1. \
        addlistener(loadBalancerListenerId=listener.id)
    config1 = admin_client.wait_success(config1)

    config2 = admin_client. \
        create_loadBalancerConfig(name=random_str())
    config2 = admin_client.wait_success(config2)
    config2 = config2. \
        addlistener(loadBalancerListenerId=listener.id)
    config2 = admin_client.wait_success(config2)

    # delete the config
    config1 = admin_client.wait_success(admin_client.delete(config1))
    assert config1.state == 'removed'

    # verify that the mapping is gone for config 1 and exists for config2
    lbconfigmap = super_client. \
        list_loadBalancerConfigListenerMap(loadBalancerListenerId=listener.id,
                                           loadBalancerConfigId=config1.id)

    assert lbconfigmap[0].state == "removed"

    lbconfigmap = super_client. \
        list_loadBalancerConfigListenerMap(loadBalancerListenerId=listener.id,
                                           loadBalancerConfigId=config2.id)

    assert lbconfigmap[0].state == "active"


def test_lb_config_remove_when_assigned(admin_client):
    config = admin_client.create_loadBalancerConfig(name=random_str())
    config = admin_client.wait_success(config)

    lb = admin_client.create_loadBalancer(name='lb',
                                          loadBalancerConfigId=config.id)
    lb = admin_client.wait_success(lb)

    with pytest.raises(ApiError) as e:
        admin_client.wait_success(admin_client.delete(config))

    assert e.value.error.status == 409
    assert e.value.error.code == 'LoadBalancerConfigIsInUse'


def test_lb_config_remove_when_used_by_removed_lb(admin_client):
    config = admin_client.create_loadBalancerConfig(name=random_str())
    config = admin_client.wait_success(config)

    lb = admin_client.create_loadBalancer(name=random_str(),
                                          loadBalancerConfigId=config.id)
    lb = admin_client.wait_success(lb)

    admin_client.wait_success(admin_client.delete(lb))

    config = admin_client.wait_success(admin_client.delete(config))

    assert config.state == "removed"


def test_lb_config_set_listeners(admin_client, super_client):
    config, listener1 = _create_config_and_listener(admin_client)
    listener2 = _create_valid_listener(admin_client)

    # set 2 listeners
    config = config.setlisteners(
        loadBalancerListenerIds=[listener1.id, listener2.id])
    config = admin_client.wait_success(config)
    assert config.state == 'active'

    lb_config_map = super_client. \
        list_loadBalancerConfigListenerMap(loadBalancerListenerId=listener1.id,
                                           loadBalancerConfigId=config.id)
    assert len(lb_config_map) == 1
    assert lb_config_map[0].state == 'active'

    lb_config_map = super_client. \
        list_loadBalancerConfigListenerMap(loadBalancerListenerId=listener2.id,
                                           loadBalancerConfigId=config.id)
    assert len(lb_config_map) == 1
    assert lb_config_map[0].state == 'active'

    # # set 1 listener
    config = config.setlisteners(loadBalancerListenerIds=[listener1.id])
    config = admin_client.wait_success(config)
    lb_config_map = super_client. \
        list_loadBalancerConfigListenerMap(loadBalancerListenerId=listener2.id,
                                           loadBalancerConfigId=config.id)

    assert lb_config_map[0].state == 'removed'

    lb_config_map = super_client. \
        list_loadBalancerConfigListenerMap(loadBalancerListenerId=listener1.id,
                                           loadBalancerConfigId=config.id)

    assert lb_config_map[0].state == 'active'

    # set 0 listener
    config = config.setlisteners(loadBalancerListenerIds=[])
    admin_client.wait_success(config)
    lb_config_map = super_client. \
        list_loadBalancerConfigListenerMap(loadBalancerListenerId=listener1.id,
                                           loadBalancerConfigId=config.id)

    assert lb_config_map[0].state == 'removed'


def _create_valid_listener(admin_client):
    listener = admin_client.create_loadBalancerListener(name=random_str(),
                                                        sourcePort='8080',
                                                        targetPort='80',
                                                        sourceProtocol='http',
                                                        targetProtocol='tcp')
    listener = admin_client.wait_success(listener)
    return listener


def _create_config_and_listener(admin_client):
    # create listener
    listener = _create_valid_listener(admin_client)
    # create config
    config = admin_client.create_loadBalancerConfig(name=random_str())
    config = admin_client.wait_success(config)
    return config, listener


def test_lb_config_add_listener_twice(admin_client, super_client):
    config, listener = _create_config_and_listener(admin_client)

    # add listener to the config
    config = config.addlistener(loadBalancerListenerId=listener.id)
    config = admin_client.wait_success(config)

    with pytest.raises(ApiError) as e:
        config.addlistener(loadBalancerListenerId=listener.id)

    assert e.value.error.status == 422
    assert e.value.error.code == 'NotUnique'
    assert e.value.error.fieldName == 'loadBalancerListenerId'


def test_lb_config_remove_invalid_listener(admin_client, super_client):
    config, listener = _create_config_and_listener(admin_client)

    # remove non-existing listener
    with pytest.raises(ApiError) as e:
        config = config. \
            removelistener(loadBalancerListenerId=listener.id)

    assert e.value.error.status == 422
    assert e.value.error.code == 'InvalidOption'
    assert e.value.error.fieldName == 'loadBalancerListenerId'


def test_lb_config_add_conflicting_listener(admin_client, super_client):
    config, listener = _create_config_and_listener(admin_client)

    # add listener to the config
    config = config.addlistener(loadBalancerListenerId=listener.id)
    config = admin_client.wait_success(config)

    assert config.state == 'active'
    lbconfigmap = super_client. \
        list_loadBalancerConfigListenerMap(loadBalancerListenerId=listener.id,
                                           loadBalancerConfigId=config.id)

    assert len(lbconfigmap) == 1
    assert lbconfigmap[0].state == 'active'

    # create duplicated listener, and try to add it to the config
    listener = _create_valid_listener(admin_client)
    with pytest.raises(ApiError) as e:
        config.addlistener(loadBalancerListenerId=listener.id)
    assert e.value.error.status == 422
    assert e.value.error.code == 'NotUnique'
    assert e.value.error.fieldName == 'sourcePort'


def test_lb_config_create_w_healthCheck(admin_client):
    health_check = {"name": "check1", "responseTimeout": 3,
                    "interval": 4, "healthyThreshold": 5,
                    "unhealthyThreshold": 6, "uri": "index.html"}
    config = admin_client.create_loadBalancerConfig(name=random_str(),
                                                    healthCheck=health_check)
    config = admin_client.wait_success(config)

    assert config.state == 'active'
    assert config.healthCheck.name == "check1"
    assert config.healthCheck.responseTimeout == 3
    assert config.healthCheck.interval == 4
    assert config.healthCheck.healthyThreshold == 5
    assert config.healthCheck.unhealthyThreshold == 6
    assert config.healthCheck.uri == "index.html"


def test_lb_config_create_disable_health_check(admin_client):
    health_check = {"name": "policy1", "responseTimeout": 3,
                    "interval": 4, "healthyThreshold": 5,
                    "unhealthyThreshold": 6, "uri": "index.html"}
    config = admin_client.create_loadBalancerConfig(name=random_str(),
                                                    healthCheck=health_check)
    config = admin_client.wait_success(config)
    assert config.healthCheck is not None

    config = admin_client.update(config, healthCheck=None)
    config = admin_client.wait_success(config)
    assert config.healthCheck is None


def test_lb_config_create_update_health_check(admin_client):
    health_check = {"name": "check1", "responseTimeout": 3,
                    "interval": 4, "healthyThreshold": 5,
                    "unhealthyThreshold": 6, "uri": "index.html"}
    config = admin_client.create_loadBalancerConfig(name=random_str(),
                                                    healthCheck=health_check)
    config = admin_client.wait_success(config)
    assert config.healthCheck.name == "check1"

    health_check = {"name": "check2", "responseTimeout": 3,
                    "interval": 4, "healthyThreshold": 5,
                    "unhealthyThreshold": 6, "uri": "index.html"}

    config = admin_client.update(config, healthCheck=health_check)
    config = admin_client.wait_success(config)
    assert config.healthCheck.name == "check2"


def test_lb_config_create_w_app_policy(admin_client):
    app_policy = {"name": "policy1", "cookie": "cookie1",
                  "length": 4, "prefix": "true",
                  "requestLearn": "false", "timeout": 10,
                  "mode": "query_string"}

    config = admin_client.\
        create_loadBalancerConfig(name=random_str(),
                                  appCookieStickinessPolicy=app_policy)
    config = admin_client.wait_success(config)

    assert config.state == 'active'
    assert config.appCookieStickinessPolicy.name == "policy1"
    assert config.appCookieStickinessPolicy.cookie == "cookie1"
    assert config.appCookieStickinessPolicy.length == 4
    assert config.appCookieStickinessPolicy.prefix is True
    assert config.appCookieStickinessPolicy.requestLearn is False
    assert config.appCookieStickinessPolicy.timeout == 10
    assert config.appCookieStickinessPolicy.mode == "query_string"

    # disable policy
    config = admin_client.\
        create_loadBalancerConfig(name=random_str(),
                                  appCookieStickinessPolicy=None)
    config = admin_client.wait_success(config)
    assert config.appCookieStickinessPolicy is None


def test_lb_config_create_w_lb_olicy(admin_client):
    lb_policy = {"name": "policy2", "cookie": "cookie1",
                 "domain": ".test.com", "indirect": "true",
                 "nocache": "true", "postonly": "true",
                 "mode": "insert"}

    config = admin_client.\
        create_loadBalancerConfig(name=random_str(),
                                  lbCookieStickinessPolicy=lb_policy)
    config = admin_client.wait_success(config)

    assert config.state == 'active'
    assert config.lbCookieStickinessPolicy.name == "policy2"
    assert config.lbCookieStickinessPolicy.cookie == "cookie1"
    assert config.lbCookieStickinessPolicy.domain == ".test.com"
    assert config.lbCookieStickinessPolicy.indirect is True
    assert config.lbCookieStickinessPolicy.nocache is True
    assert config.lbCookieStickinessPolicy.postonly is True
    assert config.lbCookieStickinessPolicy.mode == "insert"

    # disable policy
    config = admin_client.\
        create_loadBalancerConfig(name=random_str(),
                                  lbCookieStickinessPolicy=None)
    config = admin_client.wait_success(config)
    assert config.lbCookieStickinessPolicy is None
