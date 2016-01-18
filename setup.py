from distutils.core import setup
VERSION = '0.1.1'
setup(
  name = 'jokes',
  packages = ['jokes',
              'jokes.modules'],
  package_data = {'jokes':['scripts/*']},
  version = VERSION,
  description = 'Experimental language written in python',
  author = 'Kumseok Jung',
  author_email = 'jungkumseok@gmail.com',
  license = 'LICENSE',
  url = 'https://github.com/jungkumseok/jokes',
  download_url = 'https://github.com/jungkumseok/jokes/archive/'+VERSION+'.tar.gz',
  keywords = ['testing', 'language'], 
  classifiers = [],
)
