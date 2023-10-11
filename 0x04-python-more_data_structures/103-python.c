#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Function Prints basic info Python lists.
 * @p: PyObject list object.
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
        PyVarObject *var = (PyVarObject *)p;
	int size, alloc, r;
	const char *type;


	size = var->ob_size;
	alloc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (r = 0; r < size; r++)
	{
		type = list->ob_item[r]->ob_type->tp_name;
		printf("Element %d: %s\n", r, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[r]);
	}
}

/**
 * print_python_bytes - Function Prints basic info Python byte objects.
 * @p: PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	unsigned char r, size;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %d bytes: ", size);
	for (r = 0; r < size; r++)
	{
		printf("%02hhx", bytes->ob_sval[r]);
		if (r == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}
