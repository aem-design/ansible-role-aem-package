# Ansible Role: AEM Package

[![Build Status](https://travis-ci.org/aem-design/ansible-role-aem-package.svg?branch=master)](https://travis-ci.org/aem-design/ansible-role-aem-package)

Install Content Packages to AEM Instance.
> This role was developed as part of
> [AEM.Design](http://aem.design/)

## Requirements

None.

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

| Name                       	| Required 	| Default   	| Notes                                                   	|
|----------------------------	|----------	|-----------	|---------------------------------------------------------	|
| adobeaemcloud_username     	| yes      	|           	| will be used to login to adobe cloud                    	|
| adobeaemcloud_password     	| yes      	|           	| will be used to login to adobe cloud                    	|
| aem_host                   	| yes      	| localhost 	|                                                         	|
| aem_port                   	| yes      	| 4502      	|                                                         	|
| aem_username               	| yes      	| admin     	|                                                         	|
| aem_password               	| yes      	| admin     	|                                                         	|
|                            	|          	|           	|                                                         	|
| group_name                 	| yes      	|           	| group of package                                        	|
| package_name               	| yes      	|           	| package name                                            	|
| package_version            	| yes      	|           	| package name                                            	|
| package_source             	| yes      	|           	| source type used to determine how to handle package url 	|
| package_url                	| yes      	|           	| package url                                             	|
| file_name                  	| yes      	|           	| download filename                                       	|
| file_override              	| yes      	|           	| override package name that has been downloaded          	|
| file_override_package_name 	| yes      	|           	| package name to override                                	|
| simple_name                	| yes      	|           	| simple name for package                                 	|
| requires_restart           	| yes      	|           	| package restart required                                	|
| requires_admin             	| yes      	|           	| package required admin                                  	|

## Dependencies

None.

## Example Playbook

```yaml
- hosts: all
  include_role:
    name: aem-package
  vars:
    adobeaemcloud_username: "{{ adobeaemcloud_username }}"
    adobeaemcloud_password: "{{ adobeaemcloud_password }}"
    aem_host: "{{ aem_host }}"
    aem_port: "{{ aem_port }}"
    aem_username: "{{ aem_username }}"
    aem_password: "{{ aem_password }}"
    group_name: "{{ item.group_name }}"
    package_name: "{{ item.package_name }}"
    package_version: "{{ item.version }}"
    package_source: "{{ item.package_source }}"
    package_url: "{{ item.package_url }}"
    file_name: "{{ item.file_name }}"
    file_override: "{{ item.file_override | default(false) }}"
    file_override_package_name: "{{ item.file_override_package_name | default('') }}"
    simple_name: "{{ item.simple_name }}"
    requires_restart: "{{ item.requires_restart }}"
    requires_admin: "{{ item.requires_admin }}"
  with_items: "{{ package_files }}"
  when:
    - package_files is defined
    - item is defined
```

with vars

```yaml

package_files:
  ## SERVICE PACKS

  - {
    package_source: "adobecloud",
    simple_name: "adobe servicepack 1",
    file_name: 'aem-service-pkg-6.5.1.zip',
    version: '6.5.1',
    group_name: 'adobe/cq650/servicepack',
    package_name: 'aem-service-pkg',
    requires_restart: false,
    requires_admin: true,
    package_url: "https://www.adobeaemcloud.com/content/companies/public/adobe/packages/cq650/servicepack/AEM-6.5.1.0/jcr%3acontent/package/file.res/AEM-6.5.1.0-6.5.1.zip"
  }


```

## License

Apache 2.0

## Author Information

This role was created by [Max Barrass](https://aem.design/).