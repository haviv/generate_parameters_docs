Action Name: Create New Doctor

**Category:** User Management

**Description:** 

The Create New Doctor action automates the process of generating a unique Virtual Medical Assistant (VMA) account within SAP systems and assigning specific job positions to that account. Initially, it generates a unique username for the VMA based on predefined criteria, such as the SAP System Id and a username pattern for VMAs relevant to doctors. Once the VMA is successfully created, the action iterates through given positions, linking those roles to the VMA within the SAP environment using Batch Data Communication (BDC) files. This process involves interacting with SAP connectors to execute necessary actions within the SAP system. The workflow concludes by logging all action outcomes, including potential errors, thereby providing a detailed account of the operation's success or failure.

**Parameters:**

Basic:

- Name: BDC_FileName
  Description: The name of the Batch Data Communication (BDC) file which contains instructions for SAP transactions needed to assign positions to the newly created VMA.
  Default value: Not Applicable
  Mandatory: Yes

Advanced:

- Name: profileParameter_VMA
  Description: A unique identifier generated for a new Virtual Medical Assistant (VMA) that will be used in various parts of the workflow to ensure the VMA is correctly identified in all assignment and creation operations.
  Default value: Dynamically Generated
  Mandatory: Yes

**Business impact:** 

The Create New Doctor action directly impacts the efficiency and integrity of managing medical personnel identities within the SAP system. By automating the creation and assignment of VMAs to new doctors, hospitals and medical institutions can ensure rapid onboarding of medical staff, accurate role assignment, and compliance with regulatory requirements for access and identity management. This automation not only significantly reduces the manual workload involved in these processes but also minimizes the risk of human error, contributing to overall system security and compliance.

**Example of usage:** 

To use the Create New Doctor action, an administrator must initiate the workflow with the necessary parameters, including the BDC_FileName which is crucial for SAP transactions. Upon activation, the system automatically generates a VMA for a new doctor, logs the process, and associates the designated positions with the VMA through the specified BDC file. This process is executed in the background, allowing administrators to focus on other tasks while the system handles the complex SAP interactions.

**Prerequisites:** 

Users must have administrative access to the workflow system and the SAP system where the doctor's VMA will be created. They must also possess or have access to a correctly formatted BDC file with the necessary SAP transaction codes to associate the new VMA with its intended positions.

**Error Handling and Troubleshooting:** 

- **Common Error:** Failure to create VMA due to incorrect username pattern or SAP system id.
    - **Probable Cause:** Misconfiguration of the workflow parameters.
    - **Solution:** Verify and correct the workflow parameters, including the SAP system ID and the username pattern for VMAs.
  
- **Common Error:** BDC file execution failure.
    - **Probable Cause:** Incorrect BDC file name or contents.
    - **Solution:** Ensure the BDC_FileName is correct and the BDC file contains the expected SAP transaction codes for position assignments.