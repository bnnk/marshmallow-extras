
from distutils.core import setup
setup(
  name = 'mshextras',         # How you named your package folder (MyLib)
  packages = ['mshextras'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='gpl-3.0',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Extra fields for Marshmallow',   # Give a short description about your library
  author = 'BK Shrinandhan',                   # Type in your name
  author_email = 'python.access.server@gmail.ocm',      # Type in your E-Mail
  url = 'https://github.com/bnnk/marshmallow-extras',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/bnnk/marshmallow-extras/archive/master.zip',    # I explain this later on
  keywords = ['marshmallow', 'serialization', 'dumpng'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'requests',
          'marshmallow',
          'furl',
          'numpy',
          'pandas',
          'pyotp'
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Serialization',
    'License :: OSI Approved :: GNU General Public License v3.0',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
