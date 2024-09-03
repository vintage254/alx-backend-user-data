#!/usr/bin/env python3
""" authentification temlate
"""
from flask import request
from typing import List, TypeVar

User = TypeVar('User')

class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determine if authentication is required for a given path.
        :param path: The request path to check.
        :param excluded_paths: List of paths that are excluded from authentication.
        """
        if path is None or excluded_paths is None or not len(excluded_paths):
            return True
        if path[-1] != '/':
            path += '/'
        for p in excluded_paths:
            if p.endswith('*'):
                if path.startswith(p[:1]):
                    return False
        return False if path in excluded_paths else True

    def authorization_header(self, request=None) -> str:
        """
        Get the authorization header from the request.
        This is a placeholder implementation that always returns None.

        :param request: The Flask request object.
        :return: None, as the authorization header is not processed.
        """
        return None
    def current_user(self, request=None) -> User:
        """
        Get the current user based on the request.
        This is a placeholder implementation that always returns None.

        :param request: The Flask request object.
        :return: None, as the current user is not determined.
        """
        return None
