import os
import unittest

from flask import current_app
from flask_testing import TestCase

from app.main.configuration import basedir
from manage import app


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.main.configuration.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        self.assertFalse(app.config['SECRET_KEY'] == 'my_precious')
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///' + os.path.join(basedir, 'data_base_main.db')
        )


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.main.configuration.TestingConfig')
        return app

    def test_app_is_testing(self):
        self.assertFalse(app.config['SECRET_KEY'] == 'my_precious')
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///' + os.path.join(basedir, 'data_base_test.db')
        )


class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.main.configuration.ProductionConfig')
        return app

    def test_app_is_production(self):
        self.assertTrue(app.config['DEBUG'] is False)


if __name__ == '__main__':
    unittest.main()
