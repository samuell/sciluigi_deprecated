import luigi
import sciluigi as sl

class Main(sl.WorkflowTask):
    def requires(self):
        return sl.shell("echo 'foo' > <o:out:foo.txt>")

if __name__ == '__main__':
    luigi.run()
