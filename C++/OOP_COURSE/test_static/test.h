class test
{
	private:
		static int number;
	public:
		test()
		{	
			test::number ++;
		}
		int get();
};
