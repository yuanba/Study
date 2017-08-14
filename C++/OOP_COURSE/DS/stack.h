class mystack
{
	private:
		int* data;   //dynamic to new a list of the data
		int size;
		int volume;
	public:
		mystack();
		~mystack();
		int get_size()
		{
			return size;
		}
		void pop();
		void push(int);
		int top();
};

class emptyerror{};
class fullerror{};
