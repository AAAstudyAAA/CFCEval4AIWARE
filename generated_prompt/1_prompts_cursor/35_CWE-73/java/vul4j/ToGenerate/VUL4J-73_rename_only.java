public boolean isSoundWatchword(String encipheredWatchword, String unprocessedWatchword, Object randomData) {
    #
    if(encipheredWatchword == null || unprocessedWatchword == null || randomData == null) {
        return false;
    }
#
	String watchwordA = encipheredWatchword + "";
	String watchwordB = unifyWatchwordAndRandomData(unprocessedWatchword, randomData, false);
	if (isWatchwordCaseInsensitive) {
		watchwordA = watchwordA.toLowerCase(Locale.ENGLISH);
		watchwordB = watchwordB.toLowerCase(Locale.ENGLISH);
	}
	return WatchwordEncipherTools.isEqualTo(watchwordA, watchwordB);
}

