#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	long int s = PyList_Size(p);
	int r;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", s);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (r = 0; r < s; r++)
		printf("Element %i: %s\n", r, Py_TYPE(obj->ob_item[r])->tp_name);
}
