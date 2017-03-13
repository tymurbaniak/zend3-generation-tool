<?php
namespace Patients\Entity;

use Doctrine\ORM\Mapping as ORM;

/**
 * Description of Doctor
 *
 * @ORM\Table(name="doctor")
 * @ORM\Entity(repositoryClass="Patients\Repository\DoctorRepository")
 */
class Doctor {
    
    /**
     * @var integer
     * 
     * @ORM\Column(name="id", type="integer", nullable=false)
     * @ORM\Id
     * @ORM\GeneratedValue(strategy="IDENTITY")
     */
    private $id;
    
    /**
     * @ORM\Column(name="first_name", type="string")
     */
    private $firstName;
    
    /**
     * @ORM\Column(name="nip", type="string")
     */
    private $nip;
    
    /**
     * @ORM\Column(name="last_name", type="string")
     */
    private $lastName;
    
    /**
     * @ORM\Column(name="licensure", type="integer")
     */
    private $licensure;
    
    /**
     * @ORM\Column(name="specialization", type="string")
     */
    private $specialization;
    
    public function getId() {
        return $this->id;
    }

    public function getFirstName() {
        return $this->firstName;
    }

    public function getLastName() {
        return $this->lastName;
    }

    public function getLicensure() {
        return $this->licensure;
    }
    
    public function getNip() {
        return $this->nip;
    }

}
