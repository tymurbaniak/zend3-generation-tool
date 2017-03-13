import sys, re

l = []
num = 0
path = sys.argv[1]
with open(path, 'r') as f:
	for line in f:
		if "private" in line:
			l.append(re.sub('\;\\n$', '', line[13:]))
			print(line)
			num = num + 1
			

print(l)
pathsplitted = path.split("/")
namewithextension = pathsplitted[len(pathsplitted)-1]
name = re.sub('\.php$', '', namewithextension)
print(name)

#################################################################################################
#
#												Form
#
#################################################################################################
form = open(pathsplitted[0]+'/'+pathsplitted[1]+'/'+pathsplitted[2]+'/Form/'+name+'Form.php','w+')

formcontent = """
<?php
namespace """+pathsplitted[2]+"""\Form;

use Zend\Form\Form;

class """+name+"""Form extends Form{
    
    public function __construct() {
        parent::__construct('"""+name.lower()+"""-form');
        
        $this->addElements();
        $this->inputFilter();
    }
    
    public function addElements(){
"""

for field in l:
	formcontent = formcontent + """
		$this->add([
			'type' => 'text',
			'name' => '"""+re.sub(r'(\w)([A-Z0-9])', r'\1_\2', field).lower()+"""',
			'options' => [
				'label' => '',
			],
		]);
"""

formcontent = formcontent + """
        $this->add([
            'type' => 'submit',
            'name' => 'submit',
            'attributes' => [
                'value' => 'Zapisz',
            ]
        ]);
    }
    
    public function inputFilter(){
        
    }
}
"""

form.write(formcontent)
form.close()
#################################################################################################
#
#												Controller
#
#################################################################################################
controller = open(pathsplitted[0]+'/'+pathsplitted[1]+'/'+pathsplitted[2]+'/Controller/'+name+'Controller.php','w+')

controllercontent = """
<?php
namespace """+pathsplitted[1]+"""\Controller;

use Zend\Mvc\Controller\AbstractActionController;
use Zend\View\Model\ViewModel;

use """+pathsplitted[1]+"""\Entity\\"""+name+""";

use use """+pathsplitted[1]+"""\Form\\"""+name+"""Form;

class """+name+"""Controller extends AbstractActionController{
    
	private $entityManager;
	
    public function __construct($entityManager) {
        $this->entityManager = $entityManager;
    }
    
	public function indexAction(){
		$"""+name.lower()+"""s = $this->entityManager->getRepository("""+name+"""::class)
			->findAll();
		
		return new ViewModel([
			'"""+name.lower()+"""s' => $"""+name.lower()+"""s,
		]);
	}
	
	public function viewAction(){
		$id = (int) $this->params()->fromRoute('id', -1);
        if ($id<1 ) {
            $this->getResponse()->setStatusCode(404);
            return;
        }
		$"""+name.lower()+""" = $this->entityManager->getRepository("""+name+"""::class)
			->findOneById($id);
		
		return new ViewModel([
			'"""+name.lower()+"""' => $"""+name.lower()+""",
		]);
	}
	
	public function addAction(){
		$form = new """+name+"""Form();
        
        if($this->getRequest()->isPost()){
            $data = $this->params()->fromPost();
            $form->setData($data);
            if($form->isValid()){
                $data = $form->getData();
                    $this->therapyManager->add"""+name+"""($data);
                    return $this->redirect()->toRoute('', ['action'=>'index']);
            }
        }
		
		return new ViewModel([
			'form' => $form,
		]);
	}
	
	public function editAction(){
		$id = (int) $this->params()->fromRoute('id', -1);
        if ($id<1 ) {
            $this->getResponse()->setStatusCode(404);
            return;
        }
		$"""+name.lower()+""" = $this->entityManager->getRepository("""+name+"""::class)
			->findOneById($id);
			
		if($this->getRequest()->isPost()){
            $data = $this->params()->fromPost();
            $form->setData($data);
            if($form->isValid()){
                $data = $form->getData();
                    $this->therapyManager->update"""+name+"""($data);
                    return $this->redirect()->toRoute('', ['action'=>'index']);
            }
        }else{
			$form->setData([
				"""
for field in l:
	controllercontent = controllercontent + """
			'"""+re.sub(r'(\w)([A-Z0-9])', r'\1_\2', field).lower()+"""' => $"""+name.lower()+"""->get"""+field[0].upper()+field[1:]+"""(),"""
controllercontent = controllercontent + """
			]);
		}
		
		return new ViewModel([
			'form' => $form,
		]);
	}
	
	public function deleteAction(){
		$id = (int) $this->params()->fromRoute('id', -1);
        if ($id<1 ) {
            $this->getResponse()->setStatusCode(404);
            return;
        }
		$"""+name.lower()+""" = $this->entityManager->getRepository("""+name+"""::class)
			->findOneById($id);
		$this->therapyManager->delete"""+name+"""($data);
        return $this->redirect()->toRoute('', ['action'=>'index']);
	}
}	
"""
controller.write(controllercontent)
controller.close()
#################################################################################################
#
#												view
#
#################################################################################################
controller = open(pathsplitted[0]+'/'+pathsplitted[1]+'/'+pathsplitted[2]+'/Controller/'+name+'Controller.php','r')
d=[]
for line in controller:
	if "Action()" in line:
		kline =  line.split(" ")
		d.append(re.sub('Action\(\){\n', '',kline[2]))
		num = num + 1	

print(d)
for view in d:
	viewname = view
	print(view)
	viewfile = open(pathsplitted[0]+'/'+pathsplitted[1]+'/view/'+pathsplitted[1].lower()+'/'+name.lower()+'/'+viewname+'.phtml','w+')
	if (view == 'edit') or (view == 'add') :
		viewcontent = """
<?php
$this->headTitle('Dodaj tytuł!');
"""
		for field in l:
			viewcontent = viewcontent + """
			$form_>get('"""+re.sub(r'(\w)([A-Z0-9])', r'\1_\2', field).lower()+"""')->setAttributes([
			'class'=>'form-control',
			]);
			"""
		viewcontent = viewcontent + """
$doctorForm->get('submit')->setAttributes(['class'=>'btn btn-primary']);

$doctorForm->prepare();
?>
<p></p>
<div class="row">
    <div class="col-md-6">
        <?= $this->form()->openTag($form); ?>
	"""
		for field in l:
			viewcontent = viewcontent + """
			<div class="form-group">
				<?= $this->formLabel($doctorForm->get('"""+re.sub(r'(\w)([A-Z0-9])', r'\1_\2', field).lower()+"""')); ?>
				<?= $this->formElement($doctorForm->get('"""+re.sub(r'(\w)([A-Z0-9])', r'\1_\2', field).lower()+"""')); ?>
				<?= $this->formElementErrors($doctorForm->get('"""+re.sub(r'(\w)([A-Z0-9])', r'\1_\2', field).lower()+"""')); ?>
			</div>
			"""
		viewcontent = viewcontent + """
	        <?= $this->formElement($doctorForm->get('submit')); ?>
        
        <?= $this->form()->closeTag(); ?>
    </div>    
</div>   
"""
		viewfile.write(viewcontent)
		viewfile.close()