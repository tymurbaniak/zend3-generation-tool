
<?php
namespace Patients\Controller;

use Zend\Mvc\Controller\AbstractActionController;
use Zend\View\Model\ViewModel;

use Patients\Entity\Doctor;

use use Patients\Form\DoctorForm;

class DoctorController extends AbstractActionController{
    
	private $entityManager;
	
    public function __construct($entityManager) {
        $this->entityManager = $entityManager;
    }
    
	public function indexAction(){
		$doctors = $this->entityManager->getRepository(Doctor::class)
			->findAll();
		
		return new ViewModel([
			'doctors' => $doctors,
		]);
	}
	
	public function viewAction(){
		$id = (int) $this->params()->fromRoute('id', -1);
        if ($id<1 ) {
            $this->getResponse()->setStatusCode(404);
            return;
        }
		$doctor = $this->entityManager->getRepository(Doctor::class)
			->findOneById($id);
		
		return new ViewModel([
			'doctor' => $doctor,
		]);
	}
	
	public function addAction(){
		$form = new DoctorForm();
        
        if($this->getRequest()->isPost()){
            $data = $this->params()->fromPost();
            $form->setData($data);
            if($form->isValid()){
                $data = $form->getData();
                    $this->therapyManager->addDoctor($data);
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
		$doctor = $this->entityManager->getRepository(Doctor::class)
			->findOneById($id);
			
		if($this->getRequest()->isPost()){
            $data = $this->params()->fromPost();
            $form->setData($data);
            if($form->isValid()){
                $data = $form->getData();
                    $this->therapyManager->updateDoctor($data);
                    return $this->redirect()->toRoute('', ['action'=>'index']);
            }
        }else{
			$form->setData([
				
			'id' => $doctor->getId(),
			'first_name' => $doctor->getFirstName(),
			'nip' => $doctor->getNip(),
			'last_name' => $doctor->getLastName(),
			'licensure' => $doctor->getLicensure(),
			'specialization' => $doctor->getSpecialization(),
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
		$doctor = $this->entityManager->getRepository(Doctor::class)
			->findOneById($id);
		$this->therapyManager->deleteDoctor($data);
        return $this->redirect()->toRoute('', ['action'=>'index']);
	}
}	
