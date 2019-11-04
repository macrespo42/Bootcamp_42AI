if python --version = "Python 3.7.4"
then
	read -p "already installed do you want to reinstall ? [yes/no] : " response
	if test "$response" = "yes"
	then
		rm -rf ~/miniconda3
		curl "https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh" -o Miniconda_Install.sh
		bash Miniconda_Install.sh
		rm Miniconda_Install.sh
		export PATH=~/miniconda3/bin:$PATH
fi
else
	curl "https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh" -o Miniconda_Install.sh
	bash Miniconda_Install.sh
	rm Miniconda_Install.sh
	export PATH=~/miniconda3/bin:$PATH
fi
