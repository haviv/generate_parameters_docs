# Vms Rsh Filename

**Technical Name:** VmsRshFilename

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

The VmsRshFilename parameter specifies the filename of the remote shell script within the Pathlock Cloud GRC platform, specifically for use within the VMSScriptInvoker component. This filename is used to invoke specific scripts that interact with the virtual machines or services being monitored or managed.

**Business Impact:**

Proper configuration of this parameter ensures that the correct scripts are being executed for security, compliance, and risk management tasks related to virtual machines. Misconfiguration could lead to the execution of incorrect scripts, potentially affecting the monitoring and management process of the system's security and compliance protocols.

**Technical Impact when configured:**

When the VmsRshFilename is correctly set, it allows for precise control over which scripts are run, directly influencing the platform's ability to perform necessary actions on virtual machines or services such as audits, compliance checks, or security configurations. Incorrect configurations could result in failed executions, impacting the system's overall security posture and compliance status.

**Examples Scenario:**

- To ensure compliance with industry standards, an administrator configures VmsRshFilename to point to a script that verifies the configuration of virtual machines against a compliance checklist.
- For security purposes, VmsRshFilename is set to a script name that initiates a series of security checks and patches on virtual machines, mitigating vulnerabilities.

**Related Settings:**

- VMSFolder

**Best Practices:** 

- Configure when: Exact names of required scripts are known and have been tested for compatibility and correctness within the Pathlock Cloud GRC environment.
  
- Avoid when: Scripts are not fully vetted, or if there is uncertainty about the script's impact on compliance, risk, or security management operations.