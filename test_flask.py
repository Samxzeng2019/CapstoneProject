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

        self.casting_assistant_token = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjlzTjEyQlhIYTAwQjRKZW9xN0hQNyJ9.eyJpc3MiOiJodHRwczovL2Z1bGxzdGFja2lhbS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZhMGE2YjJhYzVkOTUwMDcxOTU0MzMwIiwiYXVkIjoibW92aWVzIiwiaWF0IjoxNjA0NDk4ODcyLCJleHAiOjE2MDQ1ODUyNzIsImF6cCI6Im9ENlFzNWNPbm1wcGVvWnNNdEYzTXB6TlhYcWN5QzFaIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.T2U4JeliMTjSiPWNKHVwCY2CUF_UmlRDScPHVJjB73vVDJWeIRcpW11OYNlRxUGimELt3FPx3d1qX7YFhVnfPQryjt94tEPebArEIGLQS3E46L-lB-eEFUufQV2GQ4GQkeBMsyUJZAXMrh-246bR4xB8iJK7gRNwTI19ejBlaV7OXmuNiA_CK3Z3chgLvv8QjBy4_tjPaPEBZR0PrFOoAjQahs1TekK14-biSbrXjF9EUvs6qpNXU4-lgj3I5mRIfVQHFHLNZPStgLH_FGk-26nDamymkt7mLm0VSWgn8bx4vWqlsGBWwBc7U3stn4VFthxgjpvQZMe_hF31xruMbw'
        self.casting_director_token = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjlzTjEyQlhIYTAwQjRKZW9xN0hQNyJ9.eyJpc3MiOiJodHRwczovL2Z1bGxzdGFja2lhbS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY4NmJkNTVlYWIyYzIwMDY5YzMzNjNmIiwiYXVkIjoibW92aWVzIiwiaWF0IjoxNjA0NDk4NzI2LCJleHAiOjE2MDQ1ODUxMjYsImF6cCI6Im9ENlFzNWNPbm1wcGVvWnNNdEYzTXB6TlhYcWN5QzFaIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.SMVv2fe4BEQfH4m8TkTNmFQJ2i-TV6puFsZkn-QRLihRBqZa0AjLmV9t64j2N1QMtXB3y4if8wxegBDpc3Ml70t3FZ8NQPIXxyoBdUquCJIuTq2pb-pLqoMpa2H_mIJSU8EZqkOApl2JPt_cTJGJUWV3MNKecAl03lYs9AMUqyb9waWKjQuXAOpUXXSB4ZysVE6530uttQuXK8V_RIjVmQBQk4_lTmoYOwMBxvx1ZXnvZ0bM_oALCW0NEgvXalBbaS8mdnr3hsSNLv9WNf79skZc0VLBE243k3or0YU9uwf8kDvX_Q55k-dt4zoizvrn1pKPwiFW1-uWogw1AHzL8Q'
        self.executive_director_token = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjlzTjEyQlhIYTAwQjRKZW9xN0hQNyJ9.eyJpc3MiOiJodHRwczovL2Z1bGxzdGFja2lhbS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY3MzJmOWMzYmY0MTAwMDcxNGFlZjcwIiwiYXVkIjoibW92aWVzIiwiaWF0IjoxNjA0NDk4ODA0LCJleHAiOjE2MDQ1ODUyMDQsImF6cCI6Im9ENlFzNWNPbm1wcGVvWnNNdEYzTXB6TlhYcWN5QzFaIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.t3vrOtHATHwPi1ZhxEZV2ssDWhVbpB58vb5cpB0_G7EBks3DKLUqIeZytYG8cTP19jFq80DqZdtVC1Bs-giFBoARD_-qb5gvF3T1HWj8vIlepLLWzDA7g1bpyySVtE9pigqRCQt4ymsiG9Gfe-bz6ofGsyb073w8VVZ3z8UHwuwQwZDcHiT7avXzjlbGrunCAfRjlEmRMPlFl9yVPQ7WTDMCZ77Ss8Gf1TYc2scdJvieO5Kbt_b-Vbw6JrZfYYSHmLANkkSbGfpye81U6pF9kuNDHAFNwOxlp1gqIMSSygnqtMeZlNsq2fHHCicFdBpn6lzr7lvvsJsR1yUWVAIY4Q'

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
