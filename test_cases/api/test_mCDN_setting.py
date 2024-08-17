import requests
import pytest
import conftest


class TestMCDNSetting:
    def test_create_site(self):
        pass

    def test_publish_site(self):
        pass

    def test_create_ARECORD(self):
        pass

    def test_create_CNAME(self):
        pass

    def test_enable_mCDN(self):
        pass


class TestCacheRate:
    urls = conftest.api_test_data()

    @pytest.mark.cache_hit
    @pytest.mark.parametrize("url", urls)
    def test_cache_rate_hit(self, url: str):
        # """
        # This scenario only verify the hit rate of get image files
        # :param url: image url
        # :return: None
        # """
        # res_img = requests.get(url, verify=False)
        # cache_status = res_img.headers.get('X-Mly-Cache', '')
        # assert "HIT" in cache_status
        pass