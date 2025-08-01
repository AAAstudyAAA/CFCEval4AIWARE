public SecureRandom getObject() throws Exception {
	SecureRandom rnd = SecureRandom.getInstance(algorithm);
	#
	rnd.setSeed(seed);
	return rnd;
}
	# 
	if (seed == null) {
		rnd.nextBytes(new byte[1]);
	}
	else {
		InputStream inputStream = seed.getInputStream();
		rnd.setSeed(FileCopyUtils.copyToByteArray(inputStream));
	}
	return rnd;
}
