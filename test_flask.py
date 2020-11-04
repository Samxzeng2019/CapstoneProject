import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import app
from database.models import setup_db, Movie, Actor


class CapstoneTestCase(unittest.TestCase):
    """This class represents the Capstone test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.client = self.app.test_client
        self.database_name = "database.db"
        self.project_dir = os.path.dirname(os.path.abspath(__file__))
        self.database_path = "sqlite:///{}".format(os.path.join(self.project_dir, self.database_name))
        setup_db(self.app)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.casting_assistant_token = os.environ.get('CASTING_ASSISTANT_TOKEN')
        self.casting_director_token = os.environ.get('CASTING_DIRECTOR_TOKEN')
        self.executive_director_token = os.environ.get('EXECUTIVE_DIRECTOR_TOKEN')

        self.update_movie = {
            "title": "Superman",
            "release_date": "09-Nov-2018"
        }

        self.new_movie = {
            "title": "Inception",
            "release_date": "11-Apr-2014"
        }

        self.update_actor = {
            "name": "Paul",
            "age": 44,
            "gender": "Male"
        }

        self.new_actor = {
            "name": "Kelvin",
            "age": 42,
            "gender": "Male"
        }

        self.dummy = {
            "foo": "bar"
        }


    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_post_actors_200(self):
        res = self.client().post(
            '/actors',
            headers={
                'Authorization': self.casting_director_token},
            json=self.new_actor)

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIs(type(data['actors']), dict)

    def test_patch_actors_200(self):
        res = self.client().patch(
            '/actors/1',
            headers={
                'Authorization': self.casting_director_token},
            json=self.update_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIs(type(data['actors']), dict)

    def test_get_actors_200(self):
        res = self.client().get(
            '/actors',
            headers={
                'Authorization': self.casting_assistant_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])
        self.assertIs(type(data['actors']), list)

    def test_delete_actors_200(self):
        res = self.client().delete(
            '/actors/2',
            headers={
                'Authorization': self.executive_director_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['delete'])

    def test_post_movies_200(self):
        res = self.client().post(
            '/movies',
            headers={
                'Authorization': self.executive_director_token},
            json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIs(type(data['movies']), dict)

    def test_patch_movies_200(self):
        res = self.client().patch(
            '/movies/1',
            headers={
                'Authorization': self.casting_director_token},
            json=self.update_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIs(type(data['movies']), dict)

    def test_get_movies_200(self):
        res = self.client().get(
            '/movies',
            headers={
                'Authorization': self.casting_assistant_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
        self.assertIs(type(data['movies']), list)

    def test_delete_movies_200(self):
        res = self.client().delete(
            '/movies/2',
            headers={
                'Authorization': self.executive_director_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['delete'])

    def test_patch_actors_422(self):
        res = self.client().patch(
            '/actors/1000',
            headers={
                'Authorization': self.executive_director_token},
            json=self.update_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 422)

    def test_post_actors_401(self):
        res = self.client().post(
            '/movies',
            headers={
                'Authorization': self.casting_assistant_token},
            json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 401)

    def test_post_movie_400(self):
        res = self.client().post(
            '/movies',
            headers={
                'Authorization': self.executive_director_token},
            json=self.dummy)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 400)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
