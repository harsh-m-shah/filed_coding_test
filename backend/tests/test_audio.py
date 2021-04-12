import os
import unittest
import requests
import json
from constants import SONG_TEST_DATA, PODCAST_TEST_DATA, AUDIOBOOK_TEST_DATA

BASE_API_URL = 'http://localhost:5000/api/v1'


class AudioFileTestCase(unittest.TestCase):
    def test_song_creation(self):
        data = SONG_TEST_DATA
        res = requests.post(f'{BASE_API_URL}/audioFile/song', data=json.dumps(data))
        self.assertEqual(res.status_code, 200)
        self.assertIn('id', res.json())

    def test_song_creation_invalid_data(self):
        data = {"name": "sample_song"}
        res = requests.post(f'{BASE_API_URL}/audioFile/song', data=json.dumps(data))
        self.assertEqual(res.status_code, 400)
        data = {
            "name": "sample_song",
            "duration": 300,
            "unwanted_field": "xyz"
        }
        res = requests.post(f'{BASE_API_URL}/audioFile/song', data=json.dumps(data))
        self.assertEqual(res.status_code, 400)
        data["duration"] = -10
        res = requests.post(f'{BASE_API_URL}/audioFile/song', data=json.dumps(data))
        self.assertEqual(res.status_code, 400)

    def test_podcast_creation(self):
        data = PODCAST_TEST_DATA
        res = requests.post(f'{BASE_API_URL}/audioFile/podcast', data=json.dumps(data))
        self.assertEqual(res.status_code, 200)
        self.assertIn('id', res.json())

        data["participants"] = [f"p{i}" for i in range(1, 5)]
        res = requests.post(f'{BASE_API_URL}/audioFile/podcast', data=json.dumps(data))
        self.assertEqual(res.status_code, 200)
        self.assertIn('id', res.json())

    def test_podcast_creation_invalid_data(self):
        data = {
            "name": "sample_podcast",
            "duration": 400
        }
        res = requests.post(f'{BASE_API_URL}/audioFile/podcast', data=json.dumps(data))
        self.assertEqual(res.status_code, 400)
        data["duration"] = -10
        res = requests.post(f'{BASE_API_URL}/audioFile/podcast', data=json.dumps(data))
        self.assertEqual(res.status_code, 400)
        data["host"] = "alice"
        data["duration"] = 400
        data['participants'] = [f"p{i}" for i in range(1, 12)]
        res = requests.post(f'{BASE_API_URL}/audioFile/podcast', data=json.dumps(data))
        self.assertEqual(res.status_code, 400)
        data['participants'] = [i for i in range(1, 5)]
        res = requests.post(f'{BASE_API_URL}/audioFile/podcast', data=json.dumps(data))
        self.assertEqual(res.status_code, 400)

    def test_audiobook_creation(self):
        data = AUDIOBOOK_TEST_DATA
        res = requests.post(f'{BASE_API_URL}/audioFile/audiobook', data=json.dumps(data))
        self.assertEqual(res.status_code, 200)
        self.assertIn('id', res.json())

    def test_audio_creation_invalid_data(self):
        data = {
            "title": "sample_audiobook",
            "duration": 400
        }
        res = requests.post(f'{BASE_API_URL}/audioFile/audiobook', data=json.dumps(data))
        self.assertEqual(res.status_code, 400)
        data["duration"] = -10
        res = requests.post(f'{BASE_API_URL}/audioFile/audiobook', data=json.dumps(data))
        self.assertEqual(res.status_code, 400)

    def test_song_update(self):
        data = SONG_TEST_DATA
        res = requests.post(f'{BASE_API_URL}/audioFile/song', data=json.dumps(data))
        song_id = res.json()["id"]
        data_for_update = {
            "duration": 500
        }
        res = requests.put(f'{BASE_API_URL}/audioFile/song/{song_id}', data=json.dumps(data_for_update))
        self.assertEqual(res.status_code, 200)

    def test_song_update_invalid_data(self):
        data = SONG_TEST_DATA
        res = requests.post(f'{BASE_API_URL}/audioFile/song', data=json.dumps(data))
        song_id = res.json()["id"]
        data_for_update = {
            "duration": -10
        }
        res = requests.put(f'{BASE_API_URL}/audioFile/song/{song_id}', data=json.dumps(data_for_update))
        self.assertEqual(res.status_code, 400)

    def test_podcast_update(self):
        data = PODCAST_TEST_DATA
        res = requests.post(f'{BASE_API_URL}/audioFile/podcast', data=json.dumps(data))
        podcast_id = res.json()["id"]
        data_for_update = {
            "duration": 500,
            "participants": ["a", "b", "c"]
        }
        res = requests.put(f'{BASE_API_URL}/audioFile/podcast/{podcast_id}', data=json.dumps(data_for_update))
        self.assertEqual(res.status_code, 200)

    def test_podcast_update_invalid_data(self):
        data = PODCAST_TEST_DATA
        res = requests.post(f'{BASE_API_URL}/audioFile/podcast', data=json.dumps(data))
        song_id = res.json()["id"]
        data_for_update = {
            "participants": [f"p{i}" for i in range(1, 20)]
        }
        res = requests.put(f'{BASE_API_URL}/audioFile/podcast/{song_id}', data=json.dumps(data_for_update))
        self.assertEqual(res.status_code, 400)
        data_for_update = {
            "participants": [i for i in range(1, 5)]
        }
        res = requests.put(f'{BASE_API_URL}/audioFile/podcast/{song_id}', data=json.dumps(data_for_update))
        self.assertEqual(res.status_code, 400)
        data_for_update = {
            "duration": -10
        }
        res = requests.put(f'{BASE_API_URL}/audioFile/podcast/{song_id}', data=json.dumps(data_for_update))
        self.assertEqual(res.status_code, 400)

    def test_audiobook_update(self):
        data = AUDIOBOOK_TEST_DATA
        res = requests.post(f'{BASE_API_URL}/audioFile/audiobook', data=json.dumps(data))
        audiobook_id = res.json()["id"]
        data_for_update = {
            "duration": 500,
            "narrator": "alice"
        }
        res = requests.put(f'{BASE_API_URL}/audioFile/audiobook/{audiobook_id}', data=json.dumps(data_for_update))
        self.assertEqual(res.status_code, 200)

    def test_audiobook_update_invalid_data(self):
        data = AUDIOBOOK_TEST_DATA
        res = requests.post(f'{BASE_API_URL}/audioFile/audiobook', data=json.dumps(data))
        song_id = res.json()["id"]
        data_for_update = {
            "duration": -10
        }
        res = requests.put(f'{BASE_API_URL}/audioFile/audiobook/{song_id}', data=json.dumps(data_for_update))
        self.assertEqual(res.status_code, 400)

    def test_song_delete(self):
        data = SONG_TEST_DATA
        res = requests.post(f'{BASE_API_URL}/audioFile/song', data=json.dumps(data))
        song_id = res.json()["id"]
        res = requests.delete(f'{BASE_API_URL}/audioFile/song/{song_id}')
        self.assertEqual(res.status_code, 200)
        res = requests.delete(f'{BASE_API_URL}/audioFile/song/{song_id}')
        self.assertEqual(res.status_code, 404)

    def test_podcast_delete(self):
        data = PODCAST_TEST_DATA
        res = requests.post(f'{BASE_API_URL}/audioFile/podcast', data=json.dumps(data))
        podcast_id = res.json()["id"]
        res = requests.delete(f'{BASE_API_URL}/audioFile/podcast/{podcast_id}')
        self.assertEqual(res.status_code, 200)
        res = requests.delete(f'{BASE_API_URL}/audioFile/podcast/{podcast_id}')
        self.assertEqual(res.status_code, 404)

    def test_audiobook_delete(self):
        data = AUDIOBOOK_TEST_DATA
        res = requests.post(f'{BASE_API_URL}/audioFile/audiobook', data=json.dumps(data))
        audiobook_id = res.json()["id"]
        res = requests.delete(f'{BASE_API_URL}/audioFile/audiobook/{audiobook_id}')
        self.assertEqual(res.status_code, 200)
        res = requests.delete(f'{BASE_API_URL}/audioFile/audiobook/{audiobook_id}')
        self.assertEqual(res.status_code, 404)

    def test_song_get(self):
        data = SONG_TEST_DATA
        song_ids = []
        res = requests.post(f'{BASE_API_URL}/audioFile/song', data=json.dumps(data))
        song_ids.append(res.json()["id"])
        res = requests.post(f'{BASE_API_URL}/audioFile/song', data=json.dumps(data))
        song_ids.append(res.json()["id"])
        res = requests.get(f'{BASE_API_URL}/audioFile/song/{song_ids[0]}')
        self.assertEqual(res.status_code, 200)
        songs = res.json()
        self.assertTrue(len(songs) == 1 and songs[0]["id"] == song_ids[0])
        res = requests.get(f'{BASE_API_URL}/audioFile/song')
        self.assertEqual(res.status_code, 200)
        received_ids = [song["id"] for song in res.json()]
        self.assertTrue(all(song_id in received_ids for song_id in song_ids))

    def test_podcast_get(self):
        data = PODCAST_TEST_DATA
        podcast_ids = []
        res = requests.post(f'{BASE_API_URL}/audioFile/podcast', data=json.dumps(data))
        podcast_ids.append(res.json()["id"])
        res = requests.post(f'{BASE_API_URL}/audioFile/podcast', data=json.dumps(data))
        podcast_ids.append(res.json()["id"])
        res = requests.get(f'{BASE_API_URL}/audioFile/podcast/{podcast_ids[0]}')
        self.assertEqual(res.status_code, 200)
        podcasts = res.json()
        self.assertTrue(len(podcasts) == 1 and podcasts[0]["id"] == podcast_ids[0])
        res = requests.get(f'{BASE_API_URL}/audioFile/podcast')
        self.assertEqual(res.status_code, 200)
        received_ids = [podcast["id"] for podcast in res.json()]
        self.assertTrue(all(podcast_id in received_ids for podcast_id in podcast_ids))

    def test_audiobook_get(self):
        data = AUDIOBOOK_TEST_DATA
        audiobook_ids = []
        res = requests.post(f'{BASE_API_URL}/audioFile/audiobook', data=json.dumps(data))
        audiobook_ids.append(res.json()["id"])
        res = requests.post(f'{BASE_API_URL}/audioFile/audiobook', data=json.dumps(data))
        audiobook_ids.append(res.json()["id"])
        res = requests.get(f'{BASE_API_URL}/audioFile/audiobook/{audiobook_ids[0]}')
        self.assertEqual(res.status_code, 200)
        audiobooks = res.json()
        self.assertTrue(len(audiobooks) == 1 and audiobooks[0]["id"] == audiobook_ids[0])
        res = requests.get(f'{BASE_API_URL}/audioFile/audiobook')
        self.assertEqual(res.status_code, 200)
        received_ids = [audiobook["id"] for audiobook in res.json()]
        self.assertTrue(all(audiobook_id in received_ids for audiobook_id in audiobook_ids))


if __name__ == "__main__":
    if os.environ['APP_ENV'] != "test":
        raise Exception("Please enable 'test' env to perform the tests.")
    unittest.main()
