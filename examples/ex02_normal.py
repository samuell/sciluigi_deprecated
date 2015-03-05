import luigi
import sciluigi as sl

# Define some new tasks
class WriteFooFile(sl.SciTask):
    def output(self):
        return { 'out' : luigi.LocalTarget('foo.txt') }
    def run(self):
        with self.output()['out'].open('w') as outfile:
            outfile.write('foo')

class FooToBar(sl.SciTask):
    def output(self):
        return { 'out' : luigi.LocalTarget(self.get_input('foo').path + '.bar') }
    def run(self):
        with self.get_input('foo').open() as fin, self.output()['out'].open('w') as fout:
            txt = fin.read()
            fout.write(txt.replace('foo', 'bar'))

# Create the "main" workflow task
class Main(sl.WorkflowTask):
    def requires(self):
        # Instantiate tasks
        foo = WriteFooFile()
        footobar = FooToBar()
        # Define connections
        footobar.inports['foo'] = foo.outport('out')
        # Return the last task in the chain
        return footobar

luigi.run()
