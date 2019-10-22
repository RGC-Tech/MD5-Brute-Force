from distutils.core import setup
setup(
  name = 'MD5-Brute-Force',         # How you named your package folder (MyLib)
  packages = ['MD5-Brute-Force'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'This brute forces md5 hashes with you text file and your hashes.',   # Give a short description about your library
  author = 'RGC_Tech',                   # Type in your name
  author_email = 'aaron5671.outlook@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/RGCTech-Dev/MD5-Brute-Force',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/RGCTech-Dev/MD5-Brute-Force/archive/v0.1.tar.gz',    # I explain this later on
  keywords = ['MD5', 'Brute Force', 'Cracker'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'hashlib',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Password Cracking :: MD5 Tool',
    'License :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7'
  ],
)
