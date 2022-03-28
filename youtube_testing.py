import unittest
from unittest import TestCase
from unittest.mock import patch

import YouTubeAPI


class TestYouTubeApiRequest(TestCase):

    @patch('YouTubeAPI.request_send')
    def test_youtubeAPI_request(self, mock_response):
        example_api_response = {'kind': 'youtube#searchListResponse', 'etag': 'FytLSWESLmgtWdxTbFZDtGMzHEk',
                                'nextPageToken': 'CAEQAA', 'regionCode': 'US',
                                'pageInfo': {'totalResults': 187627, 'resultsPerPage': 1}, 'items': [
                {'kind': 'youtube#searchResult', 'etag': '_b6jIJ00fLp6Q1fg79n0RRnvNNA',
                 'id': {'kind': 'youtube#video', 'videoId': 'ZWEfijp3oOU'},
                 'snippet': {'publishedAt': '2021-02-24T03:38:11Z', 'channelId': 'UC-cDt6ME2j4gRpNBkG6IF0g',
                             'title': 'Things to do in Paris TX: Texas Travel Series',
                             'description': "Most people dream of visiting the Eiffel Tower, it's just the Eiffel "
                                            "Tower I've dreamed of has a red cowboy hat on top! If you can't ...",
                             'thumbnails': {
                                 'default': {'url': 'https://i.ytimg.com/vi/ZWEfijp3oOU/default.jpg', 'width': 120,
                                             'height': 90},
                                 'medium': {'url': 'https://i.ytimg.com/vi/ZWEfijp3oOU/mqdefault.jpg', 'width': 320,
                                            'height': 180},
                                 'high': {'url': 'https://i.ytimg.com/vi/ZWEfijp3oOU/hqdefault.jpg', 'width': 480,
                                          'height':
                                              360}}, 'channelTitle': 'MyCurlyAdventures',
                             'liveBroadcastContent': 'none', 'publishTime': '2021-02-24T03:38:11Z'}}]}
        mock_response.side_effect = [example_api_response]
        test = YouTubeAPI.youtubeAPI_request("Paris", "Texas", "US")
        self.assertEqual('ZWEfijp3oOU', test)
