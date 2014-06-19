from src.action.build.builder import Builder
from src.action.push.uploader import Uploader
from src.action.extract.extractor import Extractor
from src.action.uninstall.uninstaller import Uninstaller


class Wow:
    options = {}

    def run(self, options):
        self.options = options
        if options['extract']:
            self.extract()
        elif options['install']:
            self.install()
        elif options['uninstall']:
            self.uninstall()
        elif options['build']:
            self.build()
        elif options['push']:
            self.push()
        elif options['use']:
        	self.use()

    #Extract a wow file
    def extract(self):
        extractor = Extractor()
        extractor.extract(self.options['<filename>'])

    #Download a
    def install(self):
        print('install')

    def uninstall(self):
        uninstaller = Uninstaller()
        for package in self.options['<package>']:
            uninstaller.uninstall(package)

    def build(self):
        print('Building')
        builder = Builder()
        if self.options['<platform>'] is not None:
            builder.platform = self.options['<platform>']
        builder.build()

    def push(self):
        uploader = Uploader()
        uploader.upload(self.options['<file>'][0])

    def use(self):
    	print('Using version x of package y')