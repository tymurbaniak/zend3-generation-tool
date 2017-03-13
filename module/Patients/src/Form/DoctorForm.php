
<?php
namespace src\Form;

use Zend\Form\Form;

class DoctorForm extends Form{
    
    public function __construct() {
        parent::__construct('doctor-form');
        
        $this->addElements();
        $this->inputFilter();
    }
    
    public function addElements(){

		$this->add([
			'type' => 'text',
			'name' => 'id',
			'options' => [
				'label' => '',
			],
		]);

		$this->add([
			'type' => 'text',
			'name' => 'first_name',
			'options' => [
				'label' => '',
			],
		]);

		$this->add([
			'type' => 'text',
			'name' => 'nip',
			'options' => [
				'label' => '',
			],
		]);

		$this->add([
			'type' => 'text',
			'name' => 'last_name',
			'options' => [
				'label' => '',
			],
		]);

		$this->add([
			'type' => 'text',
			'name' => 'licensure',
			'options' => [
				'label' => '',
			],
		]);

		$this->add([
			'type' => 'text',
			'name' => 'specialization',
			'options' => [
				'label' => '',
			],
		]);

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
