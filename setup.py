#!/usr/bin/env python


# Copyright 2012-2014 Keith Fancher
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from distutils.core import setup


setup(name='todo_indicator',
      version='0.5.0-1+git20170309',
      description='Ubuntu app indicator for todo.txt-style todo lists',
      author='William Blanchard, Keith Fancher',
      author_email='nick87720z@gmail.com',
      license='GPLv3',
      url='https://github.com/nick87720z/Todo-Indicator',
      packages=['todotxt'],
      package_data={'todotxt': ['img/*']},
      scripts=['todo_indicator.py'],
      install_requires=[
          'argparse',
          'pyinotify'
      ]
)
