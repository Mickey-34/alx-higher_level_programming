#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints bytes information
 i*
 * Mimi
 * @p: Python Object
 * Return: no return
 */
void print_python_bytes(PyObject *p)
{
	char *string;
	long int size, z, limit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;

	printf("  first %ld bytes:", limit);

	for (z = 0; z < limit; z++)
		if (string[z] >= 0)
			printf(" %02x", string[z]);
		else
			printf(" %02x", 256 + string[z]);

	printf("\n");
}

/**
 * print_python_list - Prints list information
 *
 * Mimi
 * @p: Python Object
 * Return: no return
 */
void print_python_list(PyObject *p)
{
	long int size, q;
	PyListObject *list;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (q = 0; q < size; q++)
	{
		obj = ((PyListObject *)p)->ob_item[q];
		printf("Element %ld: %s\n", q, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
