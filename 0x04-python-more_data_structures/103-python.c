#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Function that Prints basic info Python lists.
 * @p: PyObject list object.
 */
void print_python_list(PyObject *p)
{
	int s, alloc, r;
	const char *typ;
	PyListObject *lst = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	s = var->ob_size;
	alloc = lst->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", s);
	printf("[*] Allocated = %d\n", alloc);

	for (r = 0; r < s; r++)
	{
		typ = lst->ob_item[r]->ob_typ->tp_name;
		printf("Element %d: %s\n", r, typ);
		if (strcmp(typ, "bytes") == 0)
			print_python_bytes(lst->ob_item[r]);
	}
}

/**
 * print_python_bytes - Function Prints basic info Python byte objects.
 * @p: PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	unsigned char r, s;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  s: %ld\n", ((PyVarObject *)p)->ob_s);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_s > 10)
		s = 10;
	else
		s = ((PyVarObject *)p)->ob_s + 1;

	printf("  first %d bytes: ", s);
	for (r = 0; r < s; r++)
	{
		printf("%02hhx", bytes->ob_sval[r]);
		if (r == (s - 1))
			printf("\n");
		else
			printf(" ");
	}
}
