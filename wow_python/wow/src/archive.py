import tarfile


class Archive:
    @staticmethod
    def create(archive, files):
        with tarfile.open(archive, "w:gz") as tar:
            for filename in files:
                tar.add(filename)
            tar.close()

    @staticmethod
    def extract(archive, destination='.'):
        tar = tarfile.open(archive)
        tar.extractall(destination)
        tar.close()



